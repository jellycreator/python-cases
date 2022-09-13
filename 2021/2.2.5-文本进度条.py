progress_bar = ".................................................."
rate_of_progress = 0
while rate_of_progress <= 100:
    str_output = str(rate_of_progress) + "%[" + progress_bar +"]"
    print("========================正在下载=======================")
    print(str_output)
    rate_of_progress += 2
    progress_bar = progress_bar.replace(".","*",1)
print("========================下载完成========================")
input()