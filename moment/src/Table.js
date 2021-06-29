import React from 'react';

const TableHeader = () => { 
    return (
        <thead>
            <tr>
                <th>Date</th>
                <th>Time</th>
                <th>Event</th>
                <th>Repetition</th>
                <th>Remove</th>
            </tr>
        </thead>
    );
}

const TableBody = props => { 
    const rows = props.characterData.map((row, index) => {
        return (
            <tr key={index}>
                <td>{row.date}</td>
                <td>{row.time}</td>
                <td>{row.event}</td>
                <td>{row.rep}</td>
                <td><button onClick={() => props.removeCharacter(index)}>Delete</button></td>
            </tr>
        );
    });

    return <tbody>{rows}</tbody>;
}

const Table = (props) => {
    var { characterData, removeCharacter } = props;
    // if (!characterData) {characterData = []}
        return (
            <table>
                <TableHeader />
                <TableBody characterData={characterData} removeCharacter={removeCharacter} />
            </table>
        );
}

export default Table;