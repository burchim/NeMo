# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#############################
# Visual Speech Recognition #
#############################

# CTC
from nemo.collections.multimodal.speech_cv.models.visual_ctc_bpe_models import VisualEncDecCTCModelBPE
from nemo.collections.multimodal.speech_cv.models.visual_ctc_models import VisualEncDecCTCModel
# RNN-T
from nemo.collections.multimodal.speech_cv.models.visual_rnnt_models import VisualEncDecRNNTModel
from nemo.collections.multimodal.speech_cv.models.visual_rnnt_bpe_models import VisualEncDecRNNTBPEModel
# Hybrid CTC/RNN-T
from nemo.collections.multimodal.speech_cv.models.visual_hybrid_rnnt_ctc_models import VisualEncDecHybridRNNTCTCModel
from nemo.collections.multimodal.speech_cv.models.visual_hybrid_rnnt_ctc_bpe_models import VisualEncDecHybridRNNTCTCBPEModel

###################################
# Audio-Visual Speech Recognition #
###################################

# CTC
from nemo.collections.multimodal.speech_cv.models.av_ctc_models import AudioVisualEncDecCTCModel
from nemo.collections.multimodal.speech_cv.models.av_ctc_bpe_models import AudioVisualEncDecCTCModelBPE
# RNN-T
from nemo.collections.multimodal.speech_cv.models.av_rnnt_models import AudioVisualEncDecRNNTModel
from nemo.collections.multimodal.speech_cv.models.av_rnnt_bpe_models import AudioVisualEncDecRNNTBPEModel
# Hybrid CTC/RNN-T
from nemo.collections.multimodal.speech_cv.models.av_hybrid_rnnt_ctc_models import AudioVisualEncDecHybridRNNTCTCModel
from nemo.collections.multimodal.speech_cv.models.av_hybrid_rnnt_ctc_bpe_models import AudioVisualEncDecHybridRNNTCTCBPEModel
