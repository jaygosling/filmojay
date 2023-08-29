import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5 d-flex justify-content-center align-items-center vh-75">
			<div className="">
				<h3>Bienvenidos a</h3>
				<span id="logo">filmjay</span>
			</div>
		</div>
	);
};
