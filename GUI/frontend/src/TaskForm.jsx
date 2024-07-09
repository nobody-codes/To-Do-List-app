// import { useState } from "react";

// const TaskForm = ({ existingTask = {}, updateCallback }) => {
//     const [value, setValue] = useState(existingTask.value || "");
//     const [status, setStatus] = useState(existingTask.status || "");

//     const updating = Object.entries(existingTask).length !== 0

//     const onSubmit = async (e) => {
//         e.preventDefault()

//         const data = {
//             value,
//             status
//         }
//         const url = "http://127.0.0.1:5000/" + (updating ? `update_task/${existingTask.id}` : "create_task")
//         const options = {
//             method: updating ? "PATCH" : "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(data)
//         }
//         const response = await fetch(url, options)
//         if (response.status !== 201 && response.status !== 200) {
//             const data = await response.json()
//             alert(data.message)
//         } else {
//             updateCallback()
//         }
//     }

//     return (
//         <form onSubmit={onSubmit}>
//             <div>
//                 <label htmlFor="value">Task:</label>
//                 <input
//                     type="text"
//                     id="value"
//                     value={value}
//                     onChange={(e) => setValue(e.target.value)}
//                 />
//             </div>
//             <div>
//                 <label htmlFor="status">status:</label>
//                 <input
//                     type="text"
//                     id="status"
//                     value={status}
//                     onChange={(e) => setStatus(e.target.value)}
//                 />
//             </div>
//             <button type="submit">{updating ? "Update" : "Create"}</button>
//         </form>
//     );
// };

// export default TaskForm

import { useState } from "react";
import "./TaskForm.css";

const TaskForm = ({ existingTask = {}, updateCallback }) => {
    const [value, setValue] = useState(existingTask.value || "");
    const [status, setStatus] = useState(existingTask.status || "");

    const updating = Object.entries(existingTask).length !== 0;

    const onSubmit = async (e) => {
        e.preventDefault();

        const data = {
            value,
            status
        };
        const url = "http://127.0.0.1:5000/" + (updating ? `update_task/${existingTask.id}` : "create_task");
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        };
        const response = await fetch(url, options);
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json();
            alert(data.message);
        } else {
            updateCallback();
        }
    };

    return (
        <form onSubmit={onSubmit} className="task-form">
            <div className="form-group">
                <label htmlFor="value">Task:</label>
                <input
                    type="text"
                    id="value"
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                    className="form-input"
                />
            </div>
            <div className="form-group">
                <label htmlFor="status">Status:</label>
                <input
                    type="text"
                    id="status"
                    value={status}
                    onChange={(e) => setStatus(e.target.value)}
                    className="form-input"
                />
            </div>
            <button type="submit" className="submit-button">{updating ? "Update" : "Create"}</button>
        </form>
    );
};

export default TaskForm;
