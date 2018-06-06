%include('header.tpl')
<div class="content-wrapper">
  <section class="content-header">
    
      <div class="box box-maroon">
        <div class="box-header with-border">
          <h3 class="box-title">Restauración de copias</h3>
        </div>
        <div class="box-body">
          <form action="/restaurar3" method="post">
            <div class="form-group">
              <label>Label</label>
              <input type="text" class="form-control" placeholder="Enter ..." name="label">
            </div>
            <div class="form-group">
              <label>Directorio</label>
              <select class="form-control" name="dir">
                %for d in dirs:
			<option>{{ d }}</option>
		%end
              </select>
            </div>
            <div class="form-group">
              <label>Bucket origen (obligatorio)</label>
              <input type="text" class="form-control" placeholder="Enter ..." name="origen">
            </div>
	    <div class="form-group">
              <label>Bucket destino</label>
              <input type="text" class="form-control" placeholder="Enter ..." name="destino">
            </div>

            <div class="form-group">
              <label>Comentarios</label>
              <textarea class="form-control" rows="3" placeholder="Enter ..." name="comentario"></textarea>
            </div>
            <div class="form-group">
              <button class="btn btn-success">Add Backup</button>
            </div>
          </form>
        </div>
      </div>
    
  </section>
</div>
%include('footer.tpl')

