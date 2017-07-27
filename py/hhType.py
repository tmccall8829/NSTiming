from neuron import h

class HHCell(object):
    def __init__(self):
        self.create_sections()
        self.define_geometry()
        self.define_biophysics()
        self.insert_stim()
        self.record_data()

    def create_sections(self):
        self.soma = h.Section(name='soma')
        
    def define_geometry(self):
        self.soma.nseg = 1
        self.soma.diam = 18.8
        self.soma.L = 18.8
        self.soma.Ra = 123.0

    def define_biophysics(self):
        self.soma.insert('hh')

    def insert_stim(self):
        self.stim = h.IClamp(self.soma(0.5))
        self.stim.delay = 20
        self.stim.dur = 60
        self.stim.amp = 0.5

    def record_data(self):
        self.v_vec = h.Vector()
        self.t_vec = h.Vector()
        self.v_vec.record(self.soma(0.5)._ref_v)
        self.t_vec.record(h._ref_t)
