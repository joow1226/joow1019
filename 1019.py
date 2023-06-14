import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# 전달함수 정의
num = [100]
den = [1, 5, 6]
G = signal.TransferFunction(num, den)

# 폐루프 전달함수 계산
M = signal.TransferFunction(num, np.polyadd(den, [100]))

# 응답 곡선 계산
t, y = signal.step(M)

# 주파수 응답 계산
w, mag, phase = signal.bode(M)

# 보드선도 계산
sys = signal.TransferFunction(num, den)
_, bode_axes = plt.subplots()
bode_axes.clear()
bode_axes.grid(True)
bode_axes.semilogx(w, mag)
bode_axes.set_xlabel('Frequency [rad/s]')
bode_axes.set_ylabel('Magnitude [dB]')
bode_axes.set_title('Bode Plot - Magnitude')

# Streamlit 앱
st.title('Control Systems Analysis')
st.header('201921034 김주원')

# 폐루프 전달함수 출력
st.header('폐루프 전달함수')
st.latex(r'M(s) = \frac{100}{s^2 + 5s + 106}')

# unit step 입력의 응답곡선 출력
st.header('Unit Step 입력 응답곡선')
fig1, ax1 = plt.subplots()
ax1.plot(t, y)
ax1.set_xlabel('시간')
ax1.set_ylabel('출력')
st.pyplot(fig1)

# 주파수 응답 및 보드선도 출력
st.header('주파수 응답 및 보드선도')
fig2, (ax2_mag, ax2_phase, ax2_bd) = plt.subplots(3, 1, figsize=(6, 9))

# 주파수 응답 - 크기 (dB)
ax2_mag.semilogx(w, mag)
ax2_mag.set_xlabel('주파수')
ax2_mag.set_ylabel('크기 (dB)')
ax2_mag.grid()

# 주파수 응답 - 위상 (도)
ax2_phase.semilogx(w, phase)
ax2_phase.set_xlabel('주파수')
ax2_phase.set_ylabel('위상 (도)')
ax2_phase.grid()

# 보드선도
ax2_bd.semilogx(w, 20 * np.log10(mag))
ax2_bd.set_xlabel('주파수')
ax2_bd.set_ylabel('Magnitude [dB]')
ax2_bd.set_title('Bode Plot - Magnitude')
ax2_bd.grid()

# 그래프 간격 조정
plt.tight_layout()

st.pyplot(fig2)