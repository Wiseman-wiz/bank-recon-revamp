import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def hello_world(self):
        self.client.get(url="http://borland.com.ph:8979/bank-recon-reports/6156cdf4e09cb9569f86f03b")