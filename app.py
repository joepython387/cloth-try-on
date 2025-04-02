import streamlit as st
from PIL import Image
import os
import subprocess

absolute_path = os.getcwd() + os.sep

def make_dir():
  os.system("mkdir inputs && cd inputs && mkdir test && cd test && mkdir cloth cloth-mask image image-parse openpose-img openpose-json")

def run(cloth, model):
  make_dir()
  cloth.save("inputs/test/cloth/cloth.jpg")
  model.save("inputs/test/image/model.jpg")

  # running script to compute the predictions
  os.system("rm -rf output/")
  # run_script = os.system("python /content/clothes-virtual-try-on/run.py")

  # print(f"Run Script Results : {run_script}")
  process = subprocess.Popen(["python", "clothes-virtual-try-on/run.py", absolute_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

  # Read and print the output in real-time
  for line in process.stdout:
      print(line.strip())

  # loading output
  op = os.listdir("output")[0]
  op = Image.open(f"output/{op}")
  return op

st.title("🛍️ Clothes Virtual Try-On")

col1, col2 = st.columns(2)

with col1:
    st.markdown("👕 **Upload the Cloth Image**")
    cloth_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="cloth")
    if cloth_file:
        st.image(cloth_file, caption="🧥 Cloth Image", use_container_width=True)

with col2:
    st.markdown("🧍 **Upload the Model Image**")
    model_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], key="model")
    if model_file:
        st.image(model_file, caption="🧑 Model Image", use_container_width=True)



if st.button("✨ Generate ✨"):
    if cloth_file and model_file:
        cloth_image = Image.open(cloth_file)
        model_image = Image.open(model_file)
        result = run(cloth_image, model_image)
        if result:
            st.image(result, caption="🎉 Final Prediction", use_container_width=True)
        else:
            st.error("⚠️ No output generated.")
    else:
        st.warning("🚨 Please upload both images.")