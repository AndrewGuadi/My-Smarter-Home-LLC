from __future__ import annotations

from datetime import datetime

from . import db


class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class ServiceCategory(db.Model, TimestampMixin):
    __tablename__ = "service_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)

    services = db.relationship("Service", back_populates="category", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<ServiceCategory {self.name}>"


class Service(db.Model, TimestampMixin):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.Text, nullable=True)
    price_range = db.Column(db.String(120), nullable=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey("service_categories.id"), nullable=False
    )

    category = db.relationship("ServiceCategory", back_populates="services")

    def __repr__(self) -> str:
        return f"<Service {self.title}>"


class Project(db.Model, TimestampMixin):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160), nullable=False)
    location = db.Column(db.String(120), nullable=True)
    scope = db.Column(db.Text, nullable=True)
    before_image = db.Column(db.String(255), nullable=True)
    after_image = db.Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<Project {self.title}>"


class Review(db.Model, TimestampMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Review {self.author} ({self.rating} stars)>"


class ServiceArea(db.Model, TimestampMixin):
    __tablename__ = "service_areas"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), nullable=False, unique=True)
    county = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(2), nullable=False, default="PA")

    def __repr__(self) -> str:
        return f"<ServiceArea {self.city}, {self.state}>"
