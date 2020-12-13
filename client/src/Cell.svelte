<script>
export let cell_type;
export let cell_id;
export let cell_file;
</script>
<style>
	.text[contenteditable] {
		grid-area: wrk;
		width: 99%;
		min-height: 4em;
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
		grid-template-columns: 5% 10% 5% 10% 70%;
		grid-template-rows: auto;
		grid-template-areas: 
		"label1 text1 label2 text2 type"
		"wrk wrk wrk wrk wrk";
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
		width: 20%;
	}

</style>

<div class="cell">
	<div class="ID normal">ID :</div>
	<input class="ID_txt normal" placeholder="Default" bind:value={cell_id}>
	<div class="File label normal">File : </div>
	<input class="File_txt normal" placeholder="index.txt" bind:value={cell_file}>
	<select bind:value={cell_type} class="Type normal">
				<option value=Markdown> Markdown</option>
				<option value=Media> Media </option>
				<option value=Code> Code </option>
	</select>
	<div class="text" contenteditable>
		
			<slot></slot>
	</div>
</div>


