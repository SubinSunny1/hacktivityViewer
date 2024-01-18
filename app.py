from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import os.path
from collections import Counter

db = SQLAlchemy()

app = Flask(__name__)

db_name = 'h1Reports.db'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    client = db.Column(db.String)
    reporter = db.Column(db.String)
    category = db.Column(db.String)
    bounty = db.Column(db.Float)
    severity = db.Column(db.String)
    description = db.Column(db.String)


@app.route('/')
def index():
    data_for_bounty = list(db.session.execute(db.select(Report).with_only_columns(Report.reporter,Report.bounty,Report.id,Report.client,Report.category).order_by(desc(Report.bounty))))
    top_10_bounties = data_for_bounty[:10]

    data_for_reporters = Counter(list(db.session.execute(db.select(Report).with_only_columns(Report.reporter))))
    top_10_reporters = sorted(data_for_reporters.items(), key = lambda x:x[1], reverse=True)[0:10]

    data_for_earners = list(db.session.execute(db.select(Report).with_only_columns(Report.reporter,Report.bounty)))
    total_earnings_per_reporter ={}
    for e in data_for_earners:
        if e[0] in total_earnings_per_reporter and e[1]:
            total_earnings_per_reporter[e[0]] += e[1]
        elif e[1]:
            total_earnings_per_reporter[e[0]] = e[1]
    top_10_earners = sorted(total_earnings_per_reporter.items(), key = lambda x:x[1], reverse=True)[0:10]

    data_for_programs = list(db.session.execute(db.select(Report).with_only_columns(Report.client,Report.bounty)))
    total_earnings_per_program ={}
    for e in data_for_programs:
        if e[0] in total_earnings_per_program and e[1]:
            total_earnings_per_program[e[0]] += e[1]
        elif e[1]:
            total_earnings_per_program[e[0]] = e[1]
    top_10_programs = sorted(total_earnings_per_program.items(), key = lambda x:x[1], reverse=True)[0:10]

    data_for_top10_reported_vulnerabilities = Counter(list(db.session.execute(db.select(Report).with_only_columns(Report.category))))
    top_10_reporterd_vulnerability = sorted(data_for_top10_reported_vulnerabilities.items(), key = lambda x:x[1], reverse=True)[0:10]

    data_for_top10_rewarded_vulnerabilities = list(db.session.execute(db.select(Report).with_only_columns(Report.category,Report.bounty)))
    total_earnings_per_vulnerability ={}
    for e in data_for_top10_rewarded_vulnerabilities:
        if e[0] in total_earnings_per_vulnerability and e[1]:
            total_earnings_per_vulnerability[e[0]] += e[1]
        elif e[1]:
            total_earnings_per_vulnerability[e[0]] = e[1]
    top_10_rewarded_vulnerabilities = sorted(total_earnings_per_vulnerability.items(), key = lambda x:x[1], reverse=True)[0:10]



    return render_template("index.html", top_10_bounties=top_10_bounties, top_10_reporters=top_10_reporters, top_10_earners=top_10_earners,top_10_programs=top_10_programs, top_10_reporterd_vulnerability=top_10_reporterd_vulnerability, top_10_rewarded_vulnerabilities=top_10_rewarded_vulnerabilities)

@app.route('/searchPage')
def searchPage():
    return render_template("search_page.html")

@app.route('/search')
def search():
    q = request.args.get('q')
    print(q)

    if q:
        results = Report.query.filter(Report.id.icontains(q) | Report.title.icontains(q) | Report.client.icontains(q) | 
                            Report.reporter.icontains(q) | Report.category.icontains(q) | Report.description.icontains(q)).all()

    else:
        results = []

    return render_template("search_results.html", results=results)

@app.route('/publishedReports/<id>')
def report(id):
    try:
        report = db.session.execute(db.select(Report)
        .filter_by(id=id).order_by(Report.id)).scalar_one()
        return render_template('report.html', report=report, id=id)
#    except Exception as e:
#        error_text = "<p>The error:<br>" + str(e) + "</p>"
#        hed = '<h1>Something is broken.</h1>'
#        return hed + error_text
    except:
        return 'Report Not Published'
    
@app.route('/publishedReports/')
def publishedReports():
    reports = list(db.session.execute(db.select(Report)
             .with_only_columns(Report.id).order_by(Report.severity).distinct()))

    page = request.args.get('page',1, type=int)
    per_page = 25
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(reports) + per_page -1) // per_page

    reports_on_page = reports[start:end]

    return render_template('publishedReports.html', reports=reports, reports_on_page=reports_on_page,
                            total_pages=total_pages, page=page)

@app.route('/allPrograms/<client>')
def program(client):
    try:
        program = list(db.session.execute(db.select(Report)
        .filter_by(client=client).order_by(Report.id)).scalars())

        page = request.args.get('page',1, type=int)
        per_page = 25
        start = (page-1) * per_page
        end = start + per_page
        total_pages = (len(program) + per_page -1) // per_page

        programs_on_page = program[start:end]

        return render_template('program.html', program=program, client=client, programs_on_page=programs_on_page,
                             total_pages=total_pages, page=page)
    except:
        return 'Program Not Found'

@app.route('/allPrograms/')
def programs():
    programs = list(db.session.execute(db.select(Report)
             .with_only_columns(Report.client).order_by(Report.client).distinct()))

    page = request.args.get('page',1, type=int)
    per_page = 25
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(programs) + per_page -1) // per_page

    programs_on_page = programs[start:end]

    return render_template('allPrograms.html', programs=programs, programs_on_page=programs_on_page,
                             total_pages=total_pages, page=page)

@app.route('/allReporters/<reporter>')
def reporterName(reporter):
    try:
        reporterName = db.session.execute(db.select(Report)
        .filter_by(reporter=reporter).order_by(Report.id)).scalars()
        return render_template('reporter.html', reporter=reporter, reporterName=reporterName)
    except:
        return 'Reporter Not Found'

@app.route('/allReporters/')
def reporters():
    reporters = list(db.session.execute(db.select(Report)
             .with_only_columns(Report.reporter).order_by(Report.reporter).distinct()))
    
    page = request.args.get('page',1, type=int)
    per_page = 25
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(reporters) + per_page -1) // per_page

    reporters_on_page = reporters[start:end]

    return render_template('allReporters.html', reporters=reporters, reporters_on_page=reporters_on_page,
                            total_pages=total_pages, page=page)

@app.route('/allWeaknesses/<category>')
def weakness(category):
    try:
        weakness = list(db.session.execute(db.select(Report).filter_by(category=category).order_by(Report.id)).scalars())

        page = request.args.get('page',1, type=int)
        per_page = 25
        start = (page-1) * per_page
        end = start + per_page
        total_pages = (len(weakness) + per_page -1) // per_page

        weaknesses_on_page = weakness[start:end]

        return render_template('weakness.html', weakness=weakness, category=category, weaknesses_on_page=weaknesses_on_page,
                             total_pages=total_pages, page=page)
    except:
        return 'Weakness Not Found'

@app.route('/allWeaknesses/')
def weaknesses():
    weaknesses = list(db.session.execute(db.select(Report)
             .with_only_columns(Report.category).order_by(Report.category).distinct()))
   
    page = request.args.get('page',1, type=int)
    per_page = 25
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(weaknesses) + per_page -1) // per_page

    weaknesses_on_page = weaknesses[start:end]

    return render_template('allWeaknesses.html', weaknesses=weaknesses, weaknesses_on_page=weaknesses_on_page,
                            total_pages=total_pages, page=page)


if __name__ == '__main__':
    app.run(debug=True)