import json

import allure
from allure_commons.types import AttachmentType


def attach_request(method, url, body=None, headers=None):
    allure.attach(
        json.dumps(
            {
                "method": method,
                "url": url,
                "headers": headers or {},
                "body": body,
            },
            indent=4,
            ensure_ascii=False,
        ),
        name="Request",
        attachment_type=AttachmentType.JSON,
    )


def attach_response(response):
    try:
        body = response.json()
    except Exception:
        body = response.text

    allure.attach(
        json.dumps(
            body,
            indent=4,
            ensure_ascii=False,
        ),
        name="Response",
        attachment_type=AttachmentType.JSON,
    )

    allure.attach(
        str(response.status_code),
        name="Status Code",
        attachment_type=AttachmentType.TEXT,
    )