import speedtest

spt = speedtest.Speedtest()
spt.get_best_server()

spt_ping = spt.results.ping
spt_download = round(spt.download() / 100 / 100 , 1)
spt_upload = round(spt.upload() / 100 / 100 , 1)

print(f"Download {spt_download} \nUpload {spt_upload} \nPing {spt_ping}")
