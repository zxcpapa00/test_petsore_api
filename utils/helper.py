import allure
import json
import random
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        """В отчет прикрепляем json респонса"""
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
