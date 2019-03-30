const initialState = {
	columns: ["column1", "column2"],
	singleFunctions: [
		{
			name: "function_name1",
			args: {
				arg1: 1,
				arg2: 2,
			},
		},
	],
	cascadFunctions: [
		[
			{
				name: "function_name3",
				args: {
					arg1: 1,
					arg2: 2,
				},
			},
		],
	],
};

export default (state = initialState, action) => {
	switch (action.type) {
		default:
			return state;
	}
};
