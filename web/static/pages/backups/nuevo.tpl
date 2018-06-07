%include('header.tpl')
<div class="content-wrapper">
  <section class="content-header">
    
      <div class="box box-maroon">
        <div class="box-header with-border">
          <h3 class="box-title">Nueva copia</h3>
        </div>
        <div class="box-body">
          <form action="/nuevo2" method="post">
            <div class="form-group">
              <label>Label (al nombre se le añadirá detrás la fecha actual)</label>
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
              <select class="form-control" name="nodo">
                <option>stark</option>
                <option>pepper</option>
                <option>todos</option>
              </select>
            </div>
            <div class="form-group">
              <label>Bucket</label>
              <input type="text" class="form-control" placeholder="Enter ..." name="bucket">
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

