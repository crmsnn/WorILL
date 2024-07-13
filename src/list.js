import React from "react";
import Level from "./level";
import data from "./list2.json"

function List() {

    return(
        <div>
            {data.levels.map(level =>
                <Level place = {level.place} title = {level.title} creator = {level.creator} link = {level.link} fps = {level.fps} id = {level.id}/>
            )}


        </div>
    );
}

export default List;