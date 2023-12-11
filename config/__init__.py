# Celery 기동을 위한 설정
from .celery import app as celery_app

__all__ = ("celery_app",)