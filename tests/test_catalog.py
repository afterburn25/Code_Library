"""Standard-library checks for the reusable source catalog."""
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from search_catalog import load, search

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items=load()

    def test_manifest_fields_and_unique_ids(self):
        self.assertGreater(len(self.items),0)
        ids=[]
        for item in self.items:
            for key in ("id","category","source_repo","source_path","source_ref","status","purpose"):
                self.assertIsInstance(item.get(key),str)
                self.assertTrue(item[key].strip(), f"{item.get('id')}: empty {key}")
            self.assertTrue(item["source_repo"].startswith("afterburn25/"))
            self.assertNotIn("..",Path(item["source_path"]).parts)
            ids.append(item["id"])
        self.assertEqual(len(ids),len(set(ids)))

    def test_copied_references_exist(self):
        for item in self.items:
            path=item.get("copied_path")
            if path:
                p=ROOT / path
                self.assertTrue(p.is_file(),f"missing: {path}")
                self.assertGreater(p.stat().st_size,0)

    def test_search_is_case_insensitive(self):
        results=search(self.items,"MODEL ROUTING")
        self.assertTrue(results)
        self.assertIn("nexus-model-routing",{x["id"] for x in results})

    def test_category_filter(self):
        results=search(self.items,"",category="testing")
        self.assertTrue(results)
        self.assertTrue(all(x["category"]=="testing" for x in results))

    def test_catalog_keeps_canonical_core_references(self):
        item=next(x for x in self.items if x["id"]=="core-module-api")
        self.assertEqual(item["status"],"canonical")
        self.assertNotIn("copied_path",item)

if __name__=="__main__":
    unittest.main()
