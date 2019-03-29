import axios from "axios";

export const registerUser = () => async dispatch => {
	try {
		await axios.post("/api/auth/register", user);
		console.log("123");
	} catch (err) {
		console.log(err.response.data);
	}
};
