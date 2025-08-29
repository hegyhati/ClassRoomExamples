package rpg.view;

import rpg.model.GameStateViewer;
import rpg.presenter.Presenter;

import java.awt.Dimension;
import java.awt.Image;
import javax.swing.*;

class MapPanel extends ViewPanel{
    private int visibilityRange;
    private int tileSize;
    private final int size;
    private final int maxRange;
    private JLabel[][] mapView;
    private ImageIcon WALL_ICON, FREE_ICON, MONSTER_ICON, HERO_ICON, HERO_MONSTER_ICON, FOG_ICON, SHRINE_ICON, HERO_SHRINE_ICON; 

    private ImageIcon getScaledTile(String file) {
        return new ImageIcon(new ImageIcon("resources/tiles/" + file).getImage().getScaledInstance(tileSize, tileSize, Image.SCALE_SMOOTH));
    }

    private void resize(int range) {
        if (range <= visibilityRange) return;
        if (range > maxRange) range = maxRange;

        visibilityRange = range;
        tileSize  = size / (2*visibilityRange+1);
        mapView = new JLabel[2*visibilityRange+1][2*visibilityRange+1];

        WALL_ICON = getScaledTile("wall.png");
        FREE_ICON = getScaledTile("free.png");
        MONSTER_ICON = getScaledTile("monster.png");
        HERO_ICON = getScaledTile("hero.png");
        HERO_MONSTER_ICON = getScaledTile("heromonster.png");
        FOG_ICON = getScaledTile("fog.png");
        SHRINE_ICON = getScaledTile("shrine.png");
        HERO_SHRINE_ICON = getScaledTile("heroshrine.png");        
        
        removeAll();

        for (int row = 0; row <  2 * visibilityRange + 1 ; ++row)
            for (int col = 0; col < 2 * visibilityRange + 1; ++col) {
                JLabel tile = new JLabel();
                tile.setBounds(tileSize*col,tileSize*row, tileSize, tileSize);
                mapView[row][col] = tile;
                add(tile);
            }
    }

    MapPanel(Presenter presenter, GameStateViewer model, int size, int maxRange) {
        super(presenter, model);
        this.maxRange = maxRange;
        this.size = size;
        this.visibilityRange = 0;

        setLayout(null);
        setPreferredSize(new Dimension(size,size));

        updateView();
    }


    @Override
    public void updateView() {
        if ( visibilityRange < maxRange && model.getMaxSightRange() + 1 > visibilityRange) resize(model.getMaxSightRange()+1);

        for (int row=-visibilityRange; row <= visibilityRange; ++row)
            for (int col = -visibilityRange; col <= visibilityRange; ++col) 
                mapView[row+visibilityRange][col+visibilityRange].setIcon(
                    !model.canSee(row,col)
                    ? FOG_ICON
                    : model.canSeeWall(row, col)
                        ? WALL_ICON 
                        : model.canSeeMonster(row, col) 
                            ? MONSTER_ICON
                            : model.canSeeShrine(row, col)
                                ? SHRINE_ICON
                                : FREE_ICON
                );
                
        if (model.getHero().isAlive()) mapView[visibilityRange][visibilityRange].setIcon(
            model.canSeeMonster(0,0) 
            ? HERO_MONSTER_ICON
            : model.canSeeShrine(0, 0)
                ? HERO_SHRINE_ICON
                : HERO_ICON
        );
    }
}