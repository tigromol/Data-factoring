import React from "react";
import "./NotFoundPage.scss";

import { Link } from "react-router-dom";

const NotFoundPage = () => {
	return (
		<div className="error-msg">
			<h1>Sorry, this page isn't available.</h1>
			<p>
				The link you followed may be broken, or the page may have been removed.
				<br />
				Go back to <Link to="/">home page</Link>.
			</p>
		</div>
	);
};

export default NotFoundPage;
