# EV HW3

## Enviroment

## Repo Hierarchy
```
hw3_r13944003/  
├── README.md  
├── configs/  
│   ├── wolf_config.json  
│   └── pillow_config.json  
├── figures/  
│   └── All PSNR result figures  
└── compute_PSNR.py
```
## Selected Materials
* Sand : wolf
* Viscocity Fluid: pillow

## How to Run
For generating the wolf simulation video, run
```
python gs_simulation.py --model_path ./model/wolf-trained/ --output_path <SELECT YOUR OUTPUT DIRECTORY> --config ./config/wolf_config.json --render_img --compile_video --white_bg
``` 

For generating the pillow simulation video, run
```
python gs_simulation.py --model_path ./model/pillow2sofa-trained/ --output_path <SELECT YOUR OUTPUT DIRECTORY> --config ./config/pillow2sofa_config_foam.json --render_img --compile_video --white_bg
``` 

For generating the PSNR figures, run
```
python compute_PSNR.py <VIDEO 1> <VIDEO 2>
```

## Results

### Baseline
* Wolf (n_grid=100, substep_dt=2e-5, grid_v_damping_scale=1.0)  
Video:  [https://youtube.com/shorts/BqIn__3E154](https://youtube.com/shorts/BqIn__3E154)

* Pillow (n_grid=100, substep_dt=2e-5, grid_v_damping_scale=1.0, softening=0.1)  
Video:  [https://youtube.com/shorts/Vs5GTLbts8o](https://youtube.com/shorts/Vs5GTLbts8o)

### Different n_grid
* Wolf  
    * Videos
        * n_grid_100: [https://youtube.com/shorts/BqIn__3E154](https://youtube.com/shorts/BqIn__3E154)
        * n_grid_50: [https://youtube.com/shorts/h4eEpDx-rEM](https://youtube.com/shorts/h4eEpDx-rEM)
        * n_grid_20: [https://youtube.com/shorts/jKy5TqeSm0U](https://youtube.com/shorts/jKy5TqeSm0U)
    * PSNR
        * n_grid_100 vs n_grid_50  
            ![PSNR](figures\wolf_ngrid100_vs_ngrid50.png)
        * n_grid_100 vs n_grid_20  
            ![PSNR](figures\wolf_ngrid100_vs_ngrid20.png)
* Pillow  
    * Videos
        * n_grid_100: [https://youtube.com/shorts/Vs5GTLbts8o](https://youtube.com/shorts/Vs5GTLbts8o)
        * n_grid_50: [https://youtube.com/shorts/CPB1afqf0EA](https://youtube.com/shorts/CPB1afqf0EA)
        * n_grid_20: [https://youtube.com/shorts/ZdFrZA27hx8](https://youtube.com/shorts/ZdFrZA27hx8)
    * PSNR
        * n_grid_100 vs n_grid_50
            ![PSNR](figures\pillow_ngrid100_vs_ngrid50.png)
        * n_grid_100 vs n_grid_20  
            ![PSNR](figures\pillow_ngrid100_vs_ngrid20.png)
* Discussion
    * n_grid determines the spatial resolution of physics simulations within the MPM system. The MPM space is subdivided into n_grid × n_grid × n_grid grids, directly influencing the level of detail in the simulation. It follows a particle → grid → particle process to accurately model the physics of each particle.
    * As shown in the video, a higher n_grid value results in a more detailed simulation, bringing it closer to reality.

### Different substep_dt
* Wolf  
    * Videos
        * substep_dt 2e-5: [https://youtube.com/shorts/BqIn__3E154](https://youtube.com/shorts/BqIn__3E154)
        * substep_dt 8e-5: [https://youtube.com/shorts/6q4aCUwrXh8](https://youtube.com/shorts/6q4aCUwrXh8)
        * substep_dt 1e-4: [https://youtube.com/shorts/kko90wwQx7w](https://youtube.com/shorts/kko90wwQx7w)
    * PSNR
        * substep_dt 2e-5 vs substep_dt 8e-5  
            ![PSNR](figures\wolf_substep2e-5_vs_substep8e-5.png)
        * substep_dt 2e-5 vs substep_dt 1e-4 
            ![PSNR](figures\wolf_substep2e-5_vs_substep1e-4.png)
* Pillow  
    * Videos
        * substep_dt 2e-5: [https://youtube.com/shorts/Vs5GTLbts8o](https://youtube.com/shorts/Vs5GTLbts8o)
        * substep_dt 5e-5: [https://youtube.com/shorts/AZIxDReXpO4](https://youtube.com/shorts/AZIxDReXpO4)
        * substep_dt 1e-4: [https://youtube.com/shorts/vE61x_Vtsvg](https://youtube.com/shorts/vE61x_Vtsvg)
    * PSNR
        * substep_dt 2e-5 vs substep_dt 5e-5  
            ![PSNR](figures\pillow_substep2e-5_vs_substep5e-5.png)
        * substep_dt 2e-5 vs substep_dt 1e-4 
            ![PSNR](figures\pillow_substep2e-5_vs_substep1e-4.png)
* Discussion
    * substep_dt determines the temporal resolution of physics simulations within the MPM system. The MPM space will update the physics every substep_dt seconds.
    * If there are some physics parameters with large value, such as Young's Module E with value 1e9, we should set the substep_dt to a smaller value, or the computation along the way may exceed the float limits and causing an overflow.
    * As shown in the video, a smaller substep_dt value results in a more detailed simulation, but it also takes more time.

### Different grid_v_damping
* Wolf  
    * Videos
        * grid_v_damping 1.0: [https://youtube.com/shorts/BqIn__3E154](https://youtube.com/shorts/BqIn__3E154)
        * grid_v_damping 0.9: [https://youtube.com/shorts/CAD7RQF926U](https://youtube.com/shorts/CAD7RQF926U)
        * grid_v_damping 0.7: [https://youtube.com/shorts/zn95FT82qvA](https://youtube.com/shorts/zn95FT82qvA)
    * PSNR
        * grid_v_damping_1.0 vs grid_v_damping_0.9  
            ![PSNR](figures\wolf_vdamping0.9_vs_vdamping1.0.png)
        * grid_v_damping_0.9 vs grid_v_damping_0.7
            ![PSNR](figures\wolf_vdamping0.9_vs_vdamping0.7.png)
* Pillow  
    * Videos
        * grid_v_damping 1.0: [https://youtube.com/shorts/Vs5GTLbts8o](https://youtube.com/shorts/Vs5GTLbts8o)
        * grid_v_damping 0.9: [https://youtube.com/shorts/DcGc8hosytA](https://youtube.com/shorts/DcGc8hosytA)
        * grid_v_damping 0.7: [https://youtube.com/shorts/3X7TlmouEgo](https://youtube.com/shorts/3X7TlmouEgo)
    * PSNR
        * grid_v_damping_1.0 vs grid_v_damping_0.9  
            ![PSNR](figures\pillow_vdamping0.9_vs_vdamping1.0.png)
        * grid_v_damping_0.9 vs grid_v_damping_0.7
            ![PSNR](figures\pillow_vdamping0.7_vs_vdamping0.9.png)
* Discussion
    * grid_v_damping_scale is used to simulate kinetic energy loss caused by air resistance or friction.
    * The grid_v_damping_scale value ranges from 0 to 1, where smaller values indicate greater energy dissipation. A lower value represents a high-friction or strong-resistance environment, causing particles to settle quickly.
    * When grid_v_damping is less than 1.0, the visual differences in the physics simulation are imperceptible. In terms of PSNR, a comparison between 0.7 and 0.9 shows an average PSNR value of 39, indicating that the variations are nearly indistinguishable.



### Different softening
* Pillow  
    * Videos
        * softening_0.1: [https://youtube.com/shorts/Vs5GTLbts8o](https://youtube.com/shorts/Vs5GTLbts8o)
        * softening_0.5: [https://youtube.com/shorts/1TjBrLykdTQ](https://youtube.com/shorts/1TjBrLykdTQ)
        * softening_2.0: [https://youtube.com/shorts/tHCIgO-dA_M](https://youtube.com/shorts/tHCIgO-dA_M)
    * PSNR
        * softening_0.1 vs softening_0.5
            ![PSNR](figures\pilloe_softening0.1_vs_softening0.5.png)
        * softening_0.1 vs softening_2.0  
            ![PSNR](figures\pilloe_softening0.1_vs_softening2.0.png)
* Discussion
    * Softening is used to simulate the behavior of elastic materials after undergoing irreversible shear or tensile deformation. As the internal structure is damaged, its strength weakens, making the material more prone to further deformation.
    * In PhysGaussian, when using softening, hardening must be set to 1.
    * Since the selected materials are sand and viscous fluid, the effects of softening are barely noticeable. Only slight variations can be detected through PSNR, while the differences remain imperceptible to the naked eye.


## Bonus

* Proposal
    * PhysGaussian requires manual parameter configuration. I believe VLM can be used to identify material properties from images and automatically generate relevant parameters based on real-world conditions.
    * I found a paper called GaussianProperty, which utilizes SAM for part-based segmentation on images. Then, VLM determines the material properties of each segmented part. A predefined set of material candidates and corresponding parameters is prepared in advance, enabling automatic material generation.
    * Since GaussianProperty only provides 2D masks and their associated materials, we need to design a 2D-to-3D mapping to project these masks onto Gaussian blobs. Each blob can be mapped to masks from different viewpoints. If a blob is closest to the respective camera position, it can inherit the corresponding material. If no suitable material is assigned from any viewpoint, KNN is used to apply the material of the nearest blob as its own.
    * During experiments, we observed that when PhysGaussian performs MPM simulations, the optimal material parameters do not necessarily match real-world values. Therefore, we must adjust the material candidate parameters in GaussianProperty based on the results of PhysGaussian to ensure accurate simulations.

