package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NerfController {

	private Nerf nerf = new Nerf(true);

	@GetMapping("/status")
	public Nerf status(@RequestParam(value = "name", defaultValue = "World") String name) {
		return nerf;
	}

	@GetMapping("/set")
	public Nerf set(@RequestParam(value = "enabled") boolean status) {
		nerf.setEnabled(status);
		return nerf;
	}
}
