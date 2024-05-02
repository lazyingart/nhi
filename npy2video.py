import numpy as np
import cv2

def npy_to_video(npy_file_path, output_video_path, fps=5):
    # Load the frames from the .npy file
    frames = np.load(npy_file_path)

    print("frames.shape: ", frames.shape)
    
    # Check if frames were loaded
    if frames is None or len(frames) == 0:
        print("No frames loaded from the file.")
        return
    
    # Assume all frames are of the same shape and type
    height, width, channels = frames[0].shape
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 'MP4V' for .mp4, change 'XVID' for .avi
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    # Write frames to the video file
    for frame in frames:
        # frame might need to be converted from BGR to RGB if colors are not correct
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    # Release everything when job is finished
    out.release()
    print(f"Video saved to {output_video_path}")

if __name__ == '__main__':
    # main()
    # Example usage
    npy_file_path = r'C:\Users\eee\Projects\nhi_hardware\data\frames_output.npy'
    output_video_path = r'C:\Users\eee\Projects\nhi_hardware\data\frames_output.mp4'
    npy_to_video(npy_file_path, output_video_path)
