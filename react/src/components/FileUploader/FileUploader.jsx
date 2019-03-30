import React from "react";
import "./FileUploader.scss";

const FileUploader = () => {
	const fileSelectHandler = e => {
		const selectedFile = e.target.files[0];
		const fd = new FormData();
		fd.append("file", selectedFile, selectedFile.name);

		// this.props.uploadFile(fd);
	};

	return (
		<div className="file-uploader">
			<input
				type="file"
				onChange={fileSelectHandler}
				name="file"
				id="file"
				className="inputfile"
			/>
			<label htmlFor="file">Upload new image</label>
		</div>
	);
};

export default FileUploader;
