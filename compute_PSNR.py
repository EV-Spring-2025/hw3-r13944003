import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import argparse

def compute_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def video_psnr(video_path1, video_path2):
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    psnr_list = []
    frame_idx = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break

        if frame1.shape != frame2.shape:
            raise ValueError(f"Frame shape mismatch at frame {frame_idx}")

        psnr = compute_psnr(frame1, frame2)
        if not np.isfinite(psnr):  # 若為 inf，強制設為 60
            psnr = 60
        psnr_list.append(psnr)
        frame_idx += 1

    cap1.release()
    cap2.release()

    avg_psnr = np.mean(psnr_list)
    return psnr_list, avg_psnr

def plot_psnr(psnr_list, avg_psnr):
    plt.figure(figsize=(10, 5))
    plt.plot(psnr_list, marker='o', linestyle='-', label='Frame PSNR')
    plt.title('Frame-wise PSNR')
    plt.xlabel('Frame Index')
    plt.ylabel('PSNR (dB)')
    plt.grid(True)
    plt.text(0.05, 0.95, f'Average PSNR: {avg_psnr:.2f} dB',
             transform=plt.gca().transAxes,
             fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Compute and plot PSNR between two videos')
    parser.add_argument('video1', type=str, help='Path to first video')
    parser.add_argument('video2', type=str, help='Path to second video')
    args = parser.parse_args()

    psnr_list, avg_psnr = video_psnr(args.video1, args.video2)
    plot_psnr(psnr_list, avg_psnr)

if __name__ == "__main__":
    main()
