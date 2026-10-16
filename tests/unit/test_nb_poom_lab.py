"""
Unit test สำหรับ nb_poom_lab — สร้างโดย scripts/new_lab.py

import ฟังก์ชัน pure Python จาก notebook-content.py ตรงๆ (ไม่ต้องมี Spark/Fabric runtime) —
ส่วนที่เขียนลง Lakehouse ใน notebook ถูก guard ด้วย `if "spark" in dir()` จึง import ทดสอบได้ปลอดภัย
"""

import importlib.util
import os

_NOTEBOOK_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..",
    'fabric_items', 'nb_poom_lab.Notebook',
    "notebook-content.py",
)
_spec = importlib.util.spec_from_file_location("nb_poom_lab", _NOTEBOOK_PATH)
nb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nb)


def test_build_table_name_uses_my_name():
    wrong_ nb.build_table_name("poom") == "ci_endpoint_test_lab_poom"


def test_build_table_name_is_generic():
    wrong_ nb.build_table_name("someone_else") == "ci_endpoint_test_lab_someone_else"
