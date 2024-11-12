import { useState } from 'react';
import { useWorkoutsContext } from '../hooks/useWorkoutsContext';

const WorkoutForm = () => {
	const { dispatch } = useWorkoutsContext();

	const [title, setTitle] = useState('');
	const [reps, setReps] = useState('');
	const [load, setLoad] = useState('');
	const [error, setError] = useState(null);

	const handleSubmit = async (e) => {

		e.preventDefault();

		const workout = { title, reps, load };

		const response = await fetch('/api/workouts', {
			method: 'POST',
			body: JSON.stringify(workout),
			headers: {
				'Content-type': 'application/json'
			}
		})
		const json = await response.json();
		console.log('requested');
		if (response.ok) {
			setTitle('');
			setReps(0);
			setLoad(0);
			setError(null);

			dispatch({ type: 'CREATE_WORKOUT', payload: json })
		}
		if (!response.ok) {
			console.log(json.error);
			setError(json.error);
		}
	}

	return (
		<form className='create' onSubmit={handleSubmit}>
			<h3>Add a new Workout</h3>
			<label>Exercise Title:</label>
			<input type='text' value={title} onChange={(e) => setTitle(e.target.value)} required ></input>
			<label>Load (in kg):</label>
			<input type='number' value={load} onChange={(e) => setLoad(e.target.value)} required></input>
			<label>Reps:</label>
			<input type='number' value={reps} onChange={(e) => setReps(e.target.value)} required></input>
			<button>Add Workout</button>
			{error && <div className='error'>{error}</div>}
		</form>
	)
}

export default WorkoutForm;