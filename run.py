# coding: utf-8
import json
import re
import subprocess
import time
import configparser

import kuaishou

def get_valid_filename(name):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    # >>> get_valid_filename("john's portrait in 2004.jpg")
    >>> get_valid_filename("{self.fname}%Y-%m-%dT%H_%M_%S")
    '{self.fname}%Y-%m-%dT%H_%M_%S'
    """
    # s = str(name).strip().replace(" ", "_") #因为有些人会在主播名中间加入空格，为了避免和录播完毕自动改名冲突，所以注释掉
    s = re.sub(r"(?u)[^-\w.%{}\[\]【】「」\s]", "", str(name))
    if s in {"", ".", ".."}:
        raise RuntimeError("Could not derive file name from '%s'" % name)
    return s


if __name__ == '__main__':

    with open('config.json', 'r') as configfile:
        config = json.load(configfile)

    # 获取配置值
    ksid = config['ksid']


    while 1:
        stream_url = kuaishou.get_real_url(ksid)

        if stream_url:

            print(stream_url)
            filename = f'%Y-%m-%dT%H_%M_%S'
            filename = get_valid_filename(filename)
            fmtname = time.strftime(filename.encode("unicode-escape").decode()).encode().decode("unicode-escape")
            print(fmtname)
            output_file = '/Videos/'+fmtname+'.mp4'#'output2.mp4'

            # 构建 FFmpeg 命令
            ffmpeg_cmd = ['ffmpeg', '-i', stream_url, '-c', 'copy', output_file]
            # 执行 FFmpeg 命令
            subprocess.run(ffmpeg_cmd)
        else:
            print('失败',stream_url)
        time.sleep(15)