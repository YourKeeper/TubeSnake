"""
TUBESNAKE YOUTUBE DOWNLOADER - LICENSED UNDER THE BSD 2-CLAUSE LICENSE
Copyright 2022 Karate Skid

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import pytube
import tkinter
import tkinter.filedialog

class GUI:
	def __init__(self):
		# Creating Window object
		self.window = tkinter.Tk()
		self.window.geometry("375x375")
		self.window.title("TubeSnake - YouTube Downloader")
		self.icon = tkinter.PhotoImage(file = 'favicon.png')
		self.window.iconphoto(False, self.icon)
		self.canvas = tkinter.Canvas(self.window, width=200, height=200)

		# Adding elements to Window
		self.logo_img = tkinter.PhotoImage(file = 'logo.png')
		self.TSlabel = tkinter.Label(self.window, text="Enter the Video or Playlist ID")
		self.entry = tkinter.Entry(self.window, fg="black", bg="white", width=25)
		self.status_label = tkinter.Label(self.window, text=" ")

		# Buttons and shit
		self.button_frame = tkinter.Frame(self.window)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.columnconfigure(1, weight=1)
		self.download_mp4_button = tkinter.Button(self.button_frame, text="MP4", width=10, height=1, bg="white", fg="black", command=self.download_mp4)
		self.download_mp3_button = tkinter.Button(self.button_frame, text="MP3", width=10, height=1, bg="white", fg="black", command=self.download_mp3)
		self.download_playlist_mp4_button = tkinter.Button(self.button_frame, text="MP4 (Playlist)", width=10, height=1, bg="white", fg="black", command=self.download_playlist_mp4)
		self.download_playlist_mp3_button = tkinter.Button(self.button_frame, text="MP3 (Playlist)", width=10, height=1, bg="white", fg="black", command=self.download_playlist_mp3)
		self.close_button = tkinter.Button(self.window, text="Exit", width=10, height=1, bg="white", fg="black", command=self.window.destroy)

		# Pack it up
		self.canvas.create_image(100, 100, image=self.logo_img)
		self.canvas.pack()
		self.TSlabel.pack()
		self.entry.pack(padx=5, pady=5)
		self.status_label.pack()
		self.download_mp4_button.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)
		self.download_playlist_mp4_button.grid(row=0, column=1, sticky=tkinter.W+tkinter.E)
		self.download_mp3_button.grid(row=1, column=0, sticky=tkinter.W+tkinter.E)
		self.download_playlist_mp3_button.grid(row=1, co		self.toggle_frame = tkinter.Frame(self.window)lumn=1, sticky=tkinter.W+tkinter.E)
		self.button_frame.pack()
		self.close_button.pack()
		self.window.mainloop()

	def throw_error(self, error):
		error_msg = f"Errors have occured! Please examine the following Error output: {error} Please re-run TubeSnake with properly provided arguments, if you encounter this Error again, please report it on our GitHub @ github.com/YourKeeper/TubeSnake"
		self.status_label.configure(text="Error!")
		tkinter.messagebox.showerror(title="An Error Occured!", message=error_msg)
		self.status_label.configure(text=" ")

	def throw_warning(self):
		warning_msg = "TubeSnake will report it's Not Responding when performing a download task, PLEASE do not close TubeSnake during this process and be patient, we promise your files are downloading! :)"
		tkinter.messagebox.showwarning(title="Warning!", message=warning_msg)

	def download_mp4(self):
		video_ID = self.entry.get()
		link = f"https://www.youtube.com/watch?v={video_ID}"
		self.throw_warning()
		self.status_label.configure(text="Downloading, p		self.toggle_frame = tkinter.Frame(self.window)lease wait...")
		save_loc = tkinter.filedialog.askdirectory()

		try:
			video = pytube.YouTube(link)
			video.streams.filter(file_extension="mp4")
			video.streams.get_highest_resolution()
			video.streams.download(output_path=save_loc)
			self.status_label.configure(text=" ")
			tkinter.messagebox.showwarning(title="Download Completed!", message=f"Video downloaded and saved to {save_loc}!")
		except Exception as error:
			self.throw_error(error)

	def download_playlist_mp4(self):
		playlist_ID = self.entry.get()
		link = f"https://www.youtube.com/playlist?list={playlist_ID}"
		self.throw_warning()
		self.status_label.configure(text="Downloading, please wait...")
		save_loc = tkinter.filedialog.askdirectory()

		try:
			playlist = pytube.Playlist(link)
			for video in playlist.videos:
				video.streams.get_highest_resolution()
				video.streams.download(output_path=save_loc)
			self.status_label.configure(text=" ")
			tkinter.messagebox.showwarning(title="Download Completed!", message=f"Playlist's contents were downloaded and saved to {save_loc}!")
		except Exception as error:
			self.throw_error(error)

	def download_mp3(self):
		video_ID = self.entry.get()
		link = f"https://www.youtube.com/watch?v={video_ID}"
		self.throw_warning()
		self.status_label.configure(text="Downloading, please wait...")
		save_loc = tkinter.filedialog.askdirectory()

		try:
			video = pytube.YouTube(link)
			video.streams.filter(only_audio=True)
			video.streams.get_highest_resolution()
			video.streams.download(output_path=save_loc)
			self.status_label.configure(text=" ")
			tkinter.messagebox.showwarning(title="Download Completed!", message=f"Video downloaded and saved to {save_loc}!")
		except Exception as error:
			self.throw_error(error)

	def download_playlist_mp3(self):
		playlist_ID = self.entry.get()
		link = f"https://www.youtube.com/playlist?list={playlist_ID}"
		self.throw_warning()
		self.status_label.configure(text="Downloading, please wait...")
		save_loc = tkinter.filedialog.askdirectory()

		try:
			playlist = pytube.Playlist(link)
			for video in playlist.videos:
				video.streams.filter(only_audio=True)
				video.streams.get_highest_resolution().download(output_path=save_loc)
			self.status_label.configure(text=" ")
			tkinter.messagebox.showwarning(title="Download Completed!", message=f"Playlist's contents were downloaded and saved to {save_loc}!")
		except Exception as error:
			self.throw_error(error)

def main():
	app = GUI()

if __name__ == "__main__":
	main()
