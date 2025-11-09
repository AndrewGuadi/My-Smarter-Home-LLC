from flask import render_template

from . import bp


@bp.route("/")
def home():
    return render_template("home.html", page_title="Home")


@bp.route("/services/electrical")
def electrical_services():
    return render_template("electrical.html", page_title="Electrical Services")


@bp.route("/services/plumbing")
def plumbing_services():
    return render_template("plumbing.html", page_title="Plumbing Services")


@bp.route("/services/bath-remodel")
def bath_remodel():
    return render_template("bath_remodel.html", page_title="Bath & Remodel")


@bp.route("/projects")
def projects():
    return render_template("projects.html", page_title="Projects")


@bp.route("/reviews")
def reviews():
    return render_template("reviews.html", page_title="Reviews")


@bp.route("/service-areas")
def service_areas():
    return render_template("service_areas.html", page_title="Service Areas")


@bp.route("/about")
def about():
    return render_template("about.html", page_title="About")


@bp.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@bp.route("/financing")
def financing():
    return render_template("financing.html", page_title="Financing & Payment Options")


@bp.route("/faq")
def faq():
    return render_template("faq.html", page_title="Frequently Asked Questions")


@bp.route("/blog")
def blog():
    return render_template("blog.html", page_title="Advice & Blog")


@bp.route("/book")
def book():
    return render_template("book.html", page_title="Book Now")


@bp.route("/quote")
def quote():
    return render_template("quote.html", page_title="Get a Quote")


@bp.route("/urgent-repair")
def urgent_repair():
    return render_template("urgent_repair.html", page_title="Urgent Repair")


@bp.route("/plan-project")
def plan_project():
    return render_template("plan_project.html", page_title="Plan My Project")
