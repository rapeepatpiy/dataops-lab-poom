# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1ba71b8a-b05c-4267-9323-00c5102e9296",
# META       "default_lakehouse_name": "lh_endpoint_lab",
# META       "default_lakehouse_workspace_id": "96646dea-918f-4a68-86e9-2be468ff8f4f",
# META       "known_lakehouses": [
# META         {
# META           "id": "1ba71b8a-b05c-4267-9323-00c5102e9296"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# ===== แก้ 3 จุด: ชื่อย่อของตัวเอง (a-z ตัวเล็ก/ตัวเลข) และ GUID 2 บรรทัดด้านล่าง =====
name = "poom"


def build_table_name(learner_name):
    """ตั้งชื่อ table ปลายทางเป็น ci_endpoint_test_lab_<ชื่อ> เสมอ กันชื่อชนกับเพื่อนคนอื่น"""
    return f"ci_endpoint_test_lab_{learner_name}"


table_name = build_table_name(name)

# GUID ของ workspace/lakehouse ฝั่ง "dev-endpoint" ของคุณเอง (ที่จดไว้ใน Lab 0)
ENDPOINT_WORKSPACE_ID = "96646dea-918f-4a68-86e9-2be468ff8f4f"
ENDPOINT_LAKEHOUSE_ID = "1ba71b8a-b05c-4267-9323-00c5102e9296"

endpoint_path = (
    f"abfss://{ENDPOINT_WORKSPACE_ID}@onelake.dfs.fabric.microsoft.com"
    f"/{ENDPOINT_LAKEHOUSE_ID}/Tables/{table_name}"
)

# เขียนจริงเข้า Lakehouse เฉพาะตอนรันในเครื่องมือ Fabric (มี spark session ให้ใช้) —
# ถ้าไฟล์นี้ถูก import ไปเทสด้วย pytest (ไม่มี spark) จะข้ามส่วนนี้ไปเฉยๆ ไม่ error
if "spark" in dir():
    df = spark.createDataFrame([(1, f"hello from {name}")], ["id", "message"])
    df.write.format("delta").mode("overwrite").save(endpoint_path)
    print(f"เขียนเข้า table: {table_name}")
else:
    print(f"[dry-run นอก Fabric] จะเขียนเข้า table: {table_name} ที่ {endpoint_path}")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
