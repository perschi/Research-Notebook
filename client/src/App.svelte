<script>
import { each } from 'svelte/internal';
import { onMount } from 'svelte';

   import Cell from './Cell.svelte';
   import FileTree from './FileTree.svelte';
   let file_tree = {sub_directories:[]};
   onMount(async () => {
		const res = await fetch("./filetree");
		file_tree = await res.json();
	});


   let documents = [{name:'File1', type:'file', content:[{id:'Undefined',text:'1', type: 'Markdown', file: 'index.txt', dirty: false},
    {id:'Undefined', text:'2', type: 'Code', file: 'index.txt', dirty: false}]},
   {name:'File2', type:'file', content:[{id:'Undefined',text:'4', type: 'Markdown', file: 'index.txt', dirty: false}]}];

   function openFile(path){
      fetch("./file/".concat('path'))
      .then(respones => respones.json())
      .then(doc => documents = documents.concat(doc));
   }

   let selected_document = 0;

   
    
    

   function addCell(){
      documents[selected_document].content = documents[selected_document].content.concat({
         id:"Undefined",
         text:"New cell",
         type:"Markdown",
         file:"Index.txt",
         dirty: true
      });
   }

   function selectDocument(i){
      //alert(i)
      console.log(i);
     selected_document = i.i;
   }
</script>

<style>
.tab{
   float: left;
   background-color: gray;
   padding-right: 10px;
   border: 1px solid black;
   margin-right: 10px;
}
.tab_active{
   float: left;
   background-color: rgb(128, 73, 73);
   padding-right: 10px;
   border: 1px solid black;
   margin-right: 10px;
}
.tab:hover {
   background-color: greenyellow;
}
</style>

<h1> Research-Journal </h1>

<table style="width:100%">


   <tr>
    <th style="width:20%">Files</th>
    <th style="width:80%">
       {#each documents as {name}, i}
    <div class={i===selected_document ?"tab_active" : "tab"} on:click={() => selectDocument({i})}>{name}</div>
       {/each}

    </th>
  </tr>
  <tr>
    <td style='vertical-align: top'>
       <!--File Structure here -->
       <FileTree bind:file_tree={file_tree}/>
    </td>
    <td>
       {#each documents[selected_document].content as {text, id, type, file}}
       <Cell bind:cell_id={id} bind:cell_type={type} bind:cell_file={file}>
          {text}
      </Cell>
      {/each}
      <button type="button" style="center" on:click={addCell}>New Cell</button> 
   </td>
  </tr>
</table>

