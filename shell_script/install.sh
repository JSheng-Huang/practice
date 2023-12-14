#!/bin/bash
#
# This script provides the ability to update the
# Legacy Boot payload for supported ChromeOS devices.
#
#
# Refer to https://zhuanlan.zhihu.com/p/365764990
# Created by JSheng <jasonhuang0124@gmail.com>
#

main() {
    echo "=====开始安装====="

    ##定义安装目录(类似于configure程序,后面接的安装位置)
    INSTALLDIR=/Users/huangchuansheng/Documents/repo/practice/shell_script/installation_test

    ##创建安装目录
    if [ ! -d "$INSTALLDIR" ]; then
        mkdir -p "$INSTALLDIR"
    fi

    ##找到shell脚本和安装包分界线
    ARCHIVE=$(awk '/^_ARCHIVE_BOUNDARY_/{print NR+1;exit 0;}' "$0")

    ##从安装包中提取出程序包，并解压
    tail -n +"$ARCHIVE" "$0" >/Users/huangchuansheng/Documents/repo/practice/shell_script/installation_test/asd
    # tar -zxvf /Users/huangchuansheng/Documents/repo/practice/shell_script/test.tar.gz -C $INSTALLDIR

    echo "=====安装结束====="
    exit 0
}
main
_ARCHIVE_BOUNDARY_
