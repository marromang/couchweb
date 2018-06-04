%include('header.tpl')
<div class="content-wrapper">
  <section class="content-header">
    
      <div class="box box-maroon">
        <div class="box-header with-border">
          <h3 class="box-title">Restauración de copias</h3>
        </div>
        <div class="box-body">
          <form action="/restaurar2" method="post">
            <div class="form-group">
              <label>Label</label>
              <input type="text" class="form-control" placeholder="Enter ..." name="label">
            </div>
            <div class="form-group">
              <label>Host</label>
              <select class="form-control" name="host">
                <option>stark</option>
                <option>pepper</option>
              </select>
            </div>
            <div class="form-group">
              <label>Nodos</label>
              <select class="form-control" name="dir">
                <option>backup-21012-12123</option>
                <option>pepper</option>
                <option>todos</option>
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

