<script>
import { each } from 'svelte/internal';

   import Cell from './Cell.svelte';
   import FileTree from './FileTree.svelte';

   let cells = [{id:'Undefined',text:'1', type: 'Markdown', file: 'index.txt', dirty: false},
    {id:'Undefined', text:'2', type: 'Code', file: 'index.txt', dirty: false}];

    let file_tree = {
       name:'directory',
       depth: 0,
       type: 'directory',
       sub_directories:[
          {name:'directory2',
          type: 'directory',
          depth:1,
         sub_directories: []},
         {name:'File1',
         depth:1,
         type:'file',
         sub_directories: []}
       ]
    };

   function addCell(){
      cells = cells.concat({
         id:"Undefined",
         text:"New cell",
         type:"Markdown",
         file:"Index.txt",
         dirty: true
      });
   }
</script>

<h1> Research-Journal </h1>

<table style="width:100%">


   <tr>
    <th style="width:20%">Files</th>
    <th style="width:80%">Cells</th>
  </tr>
  <tr>
    <td style='vertical-align: top'>
       <!--File Structure here -->
       <FileTree bind:file_tree={file_tree}/>
    </td>
    <td>
       {#each cells as {text, id, type, file}}
       <Cell bind:cell_id={id} bind:cell_type={type} bind:cell_file={file}>
          {text}
      </Cell>
      {/each}
      <button type="button" style="center" on:click={addCell}>New Cell</button> 
   </td>
  </tr>
</table>

