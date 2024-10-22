"""Utility to download all kernels for competitions"""
import os
import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

all_competiotns = api.competitions_list()

cmpt = "learning-equality-curriculum-recommendations"

cmpt_kernels = api.kernels_list(page_size=100, competition=cmpt,)

kernels_path = os.path.join(
    "~", "workspace_kaggle",
    "kc-Learning_Equality_Curriculum_Recommend",
    "downloaded_notebooks"
)

i = 1
for kernel in cmpt_kernels:
    print(f"{i}: {kernel}, {kernel.ref}")
    cmd = f"kaggle k pull {kernel.ref} -m "+\
        f"-p {os.path.join(kernels_path, kernel.ref.split('/')[1])}"
    print(cmd)
    os.system(cmd)
    i += 1
# print(cmpt_krnels)

# api.kernel_pull(
#     user_name="crained",
#     kernel_slug="crained/lecr-keep-it-correlated"
# )