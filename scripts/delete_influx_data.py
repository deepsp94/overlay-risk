from influxdb_client import InfluxDBClient

client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com", token="PMsF3myWTvfVMvZ8Di-JAeGsgP7pgbAO_wRRN7Qu865f7-YOoSAPfvUheF9pQw7RQKRp-1d5iNlC7D411SCTYQ==")

delete_api = client.delete_api()

"""
Delete Data
"""
start = "1970-01-01T00:00:00Z"
stop = "2021-05-01T00:00:00Z"
delete_api.delete(start, stop, '_measurement="mem"', bucket='ovl_kv1o', org='anantsp94@gmail.com')

"""
Close client
"""
client.close()