import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_frontmatter.py"
SPEC = importlib.util.spec_from_file_location("project_validate_frontmatter", MODULE_PATH)
validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validator)


class PortalFrontmatterTests(unittest.TestCase):
    def _validate(self, metadata: str, body: str = "# 보고서\n\n본문\n") -> list[str]:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "reports" / "2026" / "개인" / "20260001-round-0001-test" / "report-01.md"
            path.parent.mkdir(parents=True)
            path.write_text(f"---\n{metadata.strip()}\n---\n{body}", encoding="utf-8")
            return validator.validate_file(path)

    def test_portal_individual_report_allows_missing_cl_and_contributions(self) -> None:
        errors = self._validate(
            """
source: asc_web
project_type: individual
project_name: 개인 프로젝트
quad_name: 개인
members: ["20260001_김하나"]
report_number: 1
date: "2026-09-16"
status: "진행 중"
portal_submission_id: "11111111-1111-4111-8111-111111111111"
"""
        )
        self.assertEqual(errors, [])

    def test_portal_team_report_allows_missing_cl_and_contributions(self) -> None:
        errors = self._validate(
            """
source: asc_web
project_type: team
project_name: 팀 프로젝트
quad_name: A조
members: ["20260001_김하나", "20260002_이둘"]
report_number: 1
date: "2026-09-16"
status: "진행 중"
portal_submission_id: "22222222-2222-4222-8222-222222222222"
"""
        )
        self.assertEqual(errors, [])

    def test_portal_report_rejects_invalid_project_type(self) -> None:
        errors = self._validate(
            """
source: asc_web
project_type: pair
project_name: 잘못된 프로젝트
quad_name: 개인
members: ["20260001_김하나"]
report_number: 1
date: "2026-09-16"
status: "진행 중"
portal_submission_id: "33333333-3333-4333-8333-333333333333"
"""
        )
        self.assertTrue(any("project_type" in error for error in errors))

    def test_legacy_report_still_requires_cl_and_contributions(self) -> None:
        errors = self._validate(
            """
project_name: 기존 프로젝트
quad_name: A조
members: ["20260001_김하나"]
report_number: 1
date: "2026-09-16"
status: "진행 중"
"""
        )
        self.assertTrue(any("cl_level" in error for error in errors))
        self.assertTrue(any("contributions" in error for error in errors))

    def test_individual_templates_have_valid_frontmatter_and_no_team_sections(self) -> None:
        root = Path(__file__).resolve().parents[1] / "templates"
        for filename in (
            "individual-project-plan-template.md",
            "individual-report-template.md",
            "individual-final-report-template.md",
        ):
            template = root / filename
            self.assertEqual(validator.validate_file(template), [], filename)
            body = template.read_text(encoding="utf-8")
            self.assertNotIn("팀원 역할 분담", body, filename)
            self.assertNotIn("팀원별 기여", body, filename)
            self.assertNotIn("개인별 기여 내역", body, filename)
            self.assertIn("학번_이름1", body, filename)


if __name__ == "__main__":
    unittest.main()
