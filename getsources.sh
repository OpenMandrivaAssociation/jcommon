#!/bin/bash
revision=$1
version=$2
if [ $# -lt 2 ]; then
  echo "usage: $0 <git-revision> <jcommon-version-number>" >&2
  echo "" >&2
  echo "example: $0 1ea10aa82e30e0d60f57e1c562281a3ac7dd5cdd 1.0.23" >&2
  exit 1
fi
  
git clone git://github.com/jfree/jcommon.git jcommon-git-master
pushd jcommon-git-master/
git archive --prefix jcommon-${version}/ --output=../jcommon-${version}.tar ${revision}
popd
rm -rf jcommon-git-master
gzip jcommon-${version}.tar 
exit 0
