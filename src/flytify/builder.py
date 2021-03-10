from typing import Optional

from flytekit import workflow, PythonFunctionTask
import flytify.io.database as db


class Builder:
    def __init__(self, job_name: str):
        self.job_name = job_name

    @staticmethod
    def init(job_name: str):
        return Builder(job_name)

    def read(self, source_query: Optional[str] = None):
        self.source_query = source_query
        return self

    def _runner_task(self, platform: str, source_uri: str) -> str:
        print(
            f"Running runner_task with job_name: {self.job_name} "
            f"and source_uri: {source_uri} on platorm: {platform}"
        )
        return "target_uri"

    def build(self):
        @workflow
        def main_wf(platform: str) -> None:
            source_uri = db.reader(source_query=self.source_query)

            runner_task = PythonFunctionTask(
                task_config=None, task_function=self._runner_task
            )
            target_uri = runner_task(platform=platform, source_uri=source_uri)

            db.writer(target_uri=target_uri)

        main_wf._name = "main_wf"
        return main_wf
