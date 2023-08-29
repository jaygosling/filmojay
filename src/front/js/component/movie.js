import React from "react";
import { Link } from "react-router-dom";

export const Movie = () => {
    return (
        <div className="bg-primary rounded rounded-5 m-4">
            <div className="row p-5 data-view d-flex justify-content-center">
                <div className="col-3">
                    <img src="https://placehold.co/300x450"></img>
                </div>
                <div className="col-3">
                    <p>Título: Toy Story</p>
                    <p>Director/a: John Lasseter</p>
                    <p>Año: 1996</p>
                    <p>Intérpretes: Tom Hanks, Tim Allen</p>
                    <p>Género: Animación, Aventuras</p>
                    <p>Productora: Pixar Studios</p>
                </div>
                <div className="col-3">
                    <p>Argumento: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                </div>
            </div>
        </div>
    );
};