<script>
    export let file_tree;
    export let selected;

    function drawTree(root, depth){
        alert('test')
    }
</script>

<style>
    .highlight:hover {
        background-color: lightblue;
    }

    .element {
        border: 1px solid black;
        background-color: white;
        margin: 1px;
    }

    .container {
        background-color: rgb(247, 247, 247);
		border: 1px solid black;
		margin: 2px;
		padding: 4px;
    }
</style>

<div class="container">
    <div class="highlight element" > {file_tree.name} </div> 

    {#each file_tree.sub_directories as {name, sub_directories, depth}}
        <div class="highlight element" style="padding-left: {(depth + 1) * 4}px;"> {name} </div> 
    {/each}

</div>

