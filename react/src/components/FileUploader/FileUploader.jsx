import React from "react";
import "./FileUploader.scss";
import { connect } from "react-redux";
import { uploadFile } from "../../actions/uploader";

const FileUploader = ({ uploadFile }) => {
	const fileSelectHandler = e => {
		const selectedFile = e.target.files[0];
		const fd = new FormData();
		fd.append("file", selectedFile, selectedFile.name);
		uploadFile(fd);
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

const mapDispatchToProps = {
	uploadFile,
};

export default connect(
	null,
	mapDispatchToProps
)(FileUploader);
