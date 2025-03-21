%% 电能质量单一扰动

clc;clear;
fs = 1e6;                           % 采样频率
T_span = .5;                        % 信号时长
Len_signal = round(T_span*fs);      % 信号长度
df = 0.1;
N_fft = 256;                        % FFT点数
t = linspace(0, T_span, Len_signal);
f_signal = 50;

% 标准信号
signal_standard = sin(2 * pi * f_signal * t);
figure(1);
plot(t, signal_standard);title('标准信号');xlabel('时间/s');ylabel('幅值/V');

% 电压暂降
signal_sag = [ones(1, 2e5), 0.3 * ones(1, 1e5), ones(1, 2e5)] .* signal_standard;
figure(2);
plot(t, signal_sag);title('电压暂降');xlabel('时间/s');ylabel('幅值/V');

% 电压暂升
signal_swell = [ones(1, 2e5), 1.6 * ones(1, 1e5), ones(1, 2e5)] .* signal_standard;
figure(3);
plot(t, signal_swell);title('电压暂升');xlabel('时间/s');ylabel('幅值/V');




