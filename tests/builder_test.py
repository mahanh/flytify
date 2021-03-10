import unittest
from flytify.builder import Builder


class BuilderTestCase(unittest.TestCase):
    def test_builder(self) -> None:
        builder_wf = (
            Builder.init(job_name="job_1")
            .read(source_query="select * from table")
            .build()
        )
        builder_wf(platform="platform_1")
