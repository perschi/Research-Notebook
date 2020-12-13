<script>
export let cell_type;
export let cell_id;
export let cell_file;
</script>
<style>
	.text[contenteditable] {
		grid-area: wrk;
		min-height: 4em;
		width: 97%;
		background-color: lightyellow;
		border: 1px solid #aaa;
		border-radius: 2px;
		padding: 4px;
		resize: vertical;
		overflow: visible;
	}

	.cell{
		background-color: lightgray;
		border-radius: 8px;
		border: 1px solid black;
		margin: 2px;
		padding: 4px;
		display: grid;
		grid-template-columns: 4% 10% 15% 3% 10% 59%;
		grid-template-rows: auto;
		grid-template-areas: 
		"label1 text1 type label2 text2 ."
		"wrk wrk wrk wrk wrk wrk";
	}

	.normal{
		margin: 2px;
		padding: 3px;
		font-size: x-small;
	}

	.ID{
		grid-area: label1;
	}
	.ID_txt{
		grid-area: text1;
	}
	.File{
		grid-area: label2;
	}
	.File_txt{
		grid-area: text2;
	}
	.Type{
		grid-area: type;
	}

</style>

<div class="cell">
	{#if cell_type!=='File'}
	<div class="ID normal">ID :</div>
	<input class="ID_txt normal" placeholder="Default" bind:value={cell_id}>
	{/if}
	{#if cell_type==='File'}
	<div class="ID normal">File : </div>
	<input class="ID_txt normal" placeholder="index.txt" bind:value={cell_file}>
	{/if}

	<select bind:value={cell_type} class="Type normal">
				<option value=File> File </option>
				<option value=Markdown> Markdown</option>
				<option value=Media> Media </option>
				<option value=Code> Code </option>
	</select>
	<div class="text" contenteditable>
		
			<slot></slot>
	</div>
</div>


