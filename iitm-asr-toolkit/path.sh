MAIN_ROOT=/home/Downloads
KALDI_ROOT=/workspaces/adapted-hi-asr-model/kaldi-toolkit
#source $MAIN_ROOT/venv/bin/activate

[ -f $KALDI_ROOT/tools/env.sh ] && . $KALDI_ROOT/tools/env.sh
export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh

LD_LIBRARY_PATH=/usr/lib32/atlas
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/tools/openfst/lib
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/tools/openfst-1.7.2/lib
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/base
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/fstext
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/gmm
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/lm
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/matrix
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$KALDI_ROOT/src/util

export LD_LIBRARY_PATH
export LC_ALL=C


