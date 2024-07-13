import React from "react";
import './level.css';

function Level({place, title, creator, link, fps, id})  {
    return(
        <div className="level">
                <h1><em>{place}</em></h1>
                <iframe width="352" height="198"
                    src={link}>
                </iframe>
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