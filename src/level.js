import React from "react";
import './level.css';

function Level({place, title, creator, link = "https://www.youtube.com/watch?v=LtlyeDAJR7A", fps, id})  {
    return(
        <div className="level">
                <h1><em>{place}</em></h1>
                <iframe title= 'showcase' src={link} width = '352px' height='198px' />
                <h2><em>{title}</em></h2>
                <h3>{creator}</h3>
                <br/>
                <br/>
                <br/>
                <br/>
                <p>FPS: {fps} ID: {id}</p>
        </div>
    );
}

export default Level;